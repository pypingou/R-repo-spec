%global packname  trapezoid
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          The Trapezoidal Distribution

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The trapezoid package provides dtrapezoid, ptrapezoid, qtrapezoid, and
rtrapezoid functions for the trapezoidal distribution.

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
%doc %{rlibdir}/trapezoid/DESCRIPTION
%doc %{rlibdir}/trapezoid/doc
%doc %{rlibdir}/trapezoid/html
%{rlibdir}/trapezoid/R
%{rlibdir}/trapezoid/INDEX
%{rlibdir}/trapezoid/Meta
%{rlibdir}/trapezoid/NAMESPACE
%{rlibdir}/trapezoid/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora