%global packname  lcmr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.6.26
Release:          1%{?dist}
Summary:          lcmr package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-statmod 

BuildRequires:    R-devel tex(latex) R-statmod 

%description
Bayesian estimation of latent class models with random effects

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
%doc %{rlibdir}/lcmr/DESCRIPTION
%doc %{rlibdir}/lcmr/html
%{rlibdir}/lcmr/R
%{rlibdir}/lcmr/help
%{rlibdir}/lcmr/INDEX
%{rlibdir}/lcmr/data
%{rlibdir}/lcmr/NAMESPACE
%{rlibdir}/lcmr/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.26-1
- initial package for Fedora