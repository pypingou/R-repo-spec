%global packname  stringr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          Make it easier to work with strings

Group:            Applications/Engineering 
License:          GPLv2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-plyr
BuildRequires:    R-plyr
BuildRequires:    R-devel tex(latex) 

%description
stringr is a set of simple wrappers that make R's string functions
more consistent, simpler and easier to use. It does this by ensuring
that: function and argument names (and positions) are consistent,
all functions deal with NA's and zero length character appropriately,
and the output data structures from each function matches the input
data structures of other functions.

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
%doc %{rlibdir}/stringr/DESCRIPTION
%doc %{rlibdir}/stringr/html
%doc %{rlibdir}/stringr/NEWS
%{rlibdir}/stringr/INDEX
%{rlibdir}/stringr/tests
%{rlibdir}/stringr/help
%{rlibdir}/stringr/NAMESPACE
%{rlibdir}/stringr/R
%{rlibdir}/stringr/Meta

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora
