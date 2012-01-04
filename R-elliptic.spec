%global packname  elliptic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.8
Release:          1%{?dist}
Summary:          elliptic functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-emulator R-calibrator R-MASS 

BuildRequires:    R-devel tex(latex) R-emulator R-calibrator R-MASS 

%description
A suite of elliptic and related functions including Weierstrass and Jacobi
forms.  Also includes various tools for manipulating and visualizing
complex functions.

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
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.8-1
- initial package for Fedora