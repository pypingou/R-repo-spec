%global packname  gsubfn
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.7
Release:          1%{?dist}
Summary:          Utilities for strings and function arguments.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-proto 


BuildRequires:    R-devel tex(latex) R-proto



%description
gsubfn is like gsub but can take a replacement function or certain other
objects instead of the replacement string. Matches and back references are
input to the replacement function and replaced by the function output. 
gsubfn can be used to split strings based on content rather than
delimiters and for quasi-perl-style string interpolation. The package also
has facilities for translating formulas to functions and allowing such
formulas in function calls instead of functions. This can be used with R
functions such as apply, sapply, lapply, optim, integrate, xyplot, Filter
and any other function that expects another function as an input argument
or functions like cat or sql calls that may involve strings where
substitution is desirable.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.7-1
- initial package for Fedora