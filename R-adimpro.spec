%global packname  adimpro
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.5
Release:          1%{?dist}
Summary:          Adaptive Smoothing of Digital Images

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-grDevices 

BuildRequires:    R-devel tex(latex) R-grDevices 

%description
This package implements tools for manipulationg digital images and the
Propagation Separation approach by Polzehl and Spokoiny (2006) for
smoothing digital images.

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.5-1
- initial package for Fedora