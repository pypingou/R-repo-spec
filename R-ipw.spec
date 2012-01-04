%global packname  ipw
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.10
Release:          1%{?dist}
Summary:          Estimate inverse probability weights.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-boot R-geepack R-MASS R-nlme R-nnet R-survey R-survival 


BuildRequires:    R-devel tex(latex) R-boot R-geepack R-MASS R-nlme R-nnet R-survey R-survival



%description
Estimate inverse probability weights. These are typically used to perform
inverse probability weighting (IPW) to fit a marginal structural model
(MSM), to estimate causal effects from observational data. Both data from
point treatment situations and longitudinal studies can be used.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.10-1
- initial package for Fedora