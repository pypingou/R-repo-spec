%global packname  binGroup
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Evaluation and experimental design for binomial group testing

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package provides methods for estimation and hypothesis testing of
proportions in group testing designs. It involves methods for estimating a
proportion in a single population (assuming sensitivity and specificty 1
in designs with equal group sizes), as well as hypothesis tests and
functions for experimental design for this situation. For estimating one
proportion or the difference of proportions, a number of confidence
interval methods are included, which can deal with various different pool
sizes. Further, regression methods are implemented for simple pooling and
matrix pooling designs.

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
%doc %{rlibdir}/binGroup/html
%doc %{rlibdir}/binGroup/DESCRIPTION
%{rlibdir}/binGroup/data
%{rlibdir}/binGroup/help
%{rlibdir}/binGroup/INDEX
%{rlibdir}/binGroup/NAMESPACE
%{rlibdir}/binGroup/Meta
%{rlibdir}/binGroup/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora