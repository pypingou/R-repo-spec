%global packname  gsarima
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.2
Release:          1%{?dist}
Summary:          Two functions for Generalized SARIMA time series simulation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Write SARIMA models in (finite) AR representation and simulate generalized
multiplicative seasonal autoregressive moving average (time) series with
Normal / Gaussian, Poisson or negative binomial distribution.

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
%doc %{rlibdir}/gsarima/DESCRIPTION
%doc %{rlibdir}/gsarima/html
%{rlibdir}/gsarima/INDEX
%{rlibdir}/gsarima/R
%{rlibdir}/gsarima/NAMESPACE
%{rlibdir}/gsarima/help
%{rlibdir}/gsarima/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.2-1
- initial package for Fedora