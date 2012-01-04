%global packname  Rstem
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.1
Release:          1%{?dist}
Summary:          Interface to Snowball implementation of Porter's word stemming algorithm.

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
An R interface to the C code that implements Porter's word stemming
algorithm for collapsing words to a common root to aid comparison of
texts.  There is code to for different languages (i.e. danish, dutch,
english, finnish, french, german, norwegian, portuguese, russian, spanish,
swedish). However, these may not be applicable if the words require UTF
encoding. This is extensible by allowing different routines to be
specified to create the C routines used in the stemming, permitting
debugging, profiling, pool management, caching, etc.

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
%doc %{rlibdir}/Rstem/html
%doc %{rlibdir}/Rstem/DESCRIPTION
%doc %{rlibdir}/Rstem/doc
%{rlibdir}/Rstem/scripts
%{rlibdir}/Rstem/libs
%{rlibdir}/Rstem/words
%{rlibdir}/Rstem/Meta
%{rlibdir}/Rstem/NAMESPACE
%{rlibdir}/Rstem/R
%{rlibdir}/Rstem/INDEX
%{rlibdir}/Rstem/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.1-1
- initial package for Fedora