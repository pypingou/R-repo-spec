%global packname  lcmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.1
Release:          1%{?dist}
Summary:          Estimation of various latent class mixed models and joint latent class mixed models

Group:            Applications/Engineering 
License:          GPL (>= 2.0)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
This package provides functions for the estimation of various latent class
mixed models and joint latent latent class mixed models using a maximum
likelihood method

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
%doc %{rlibdir}/lcmm/html
%doc %{rlibdir}/lcmm/DESCRIPTION
%{rlibdir}/lcmm/R
%{rlibdir}/lcmm/libs
%{rlibdir}/lcmm/data
%{rlibdir}/lcmm/INDEX
%{rlibdir}/lcmm/Meta
%{rlibdir}/lcmm/help
%{rlibdir}/lcmm/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.1-1
- initial package for Fedora