%global packname  gb
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.11.24
Release:          1%{?dist}
Summary:          Generalize Lambda Distribution and Generalized Bootstrapping

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0.11-24.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
This package collects algorithms and functions for fitting data to a
generalized lambda distribution via moment matching methods, and
generalized bootstrapping.

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
%doc %{rlibdir}/gb/DESCRIPTION
%doc %{rlibdir}/gb/LICENCE
%doc %{rlibdir}/gb/html
%{rlibdir}/gb/R
%{rlibdir}/gb/help
%{rlibdir}/gb/NAMESPACE
%{rlibdir}/gb/Meta
%{rlibdir}/gb/INDEX
%{rlibdir}/gb/data
%{rlibdir}/gb/libs

%changelog
* Mon Dec 05 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.11.24-1
- initial package for Fedora