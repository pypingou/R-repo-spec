%global packname  bootstrap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.22
Release:          1%{?dist}
Summary:          Functions for the Book "An Introduction to the Bootstrap"

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-22.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats 

BuildRequires:    R-devel tex(latex) R-stats 

%description
Software (bootstrap, cross-validation, jackknife) and data for the book
"An Introduction to the Bootstrap" by B. Efron and R. Tibshirani, 1993,
Chapman and Hall.
_____________________________________________________________ This package
is primarily provided for projects already based on it, and for support of
the book.  New projects should preferentially use the recommended package

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
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.22-1
- initial package for Fedora