%global packname  haplo.ccs
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Estimate Haplotype Relative Risks in Case-Control Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-haplo.stats R-survival 

BuildRequires:    R-devel tex(latex) R-haplo.stats R-survival 

%description
'haplo.ccs' estimates haplotype and covariate relative risks in
case-control data by weighted logistic regression. Diplotype
probabilities, which are estimated by EM computation with progressive
insertion of loci, are utilized as weights.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/haplo.ccs/html
%doc %{rlibdir}/haplo.ccs/DESCRIPTION
%{rlibdir}/haplo.ccs/INDEX
%{rlibdir}/haplo.ccs/Meta
%{rlibdir}/haplo.ccs/R
%{rlibdir}/haplo.ccs/help
%{rlibdir}/haplo.ccs/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora