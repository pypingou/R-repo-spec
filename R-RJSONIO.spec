%global packname  RJSONIO
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.96.0
Release:          1%{?dist}
Summary:          Serialize R objects to JSON, JavaScript Object Notation

Group:            Applications/Engineering 
License:          BSD
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.96-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
This is a package that allows conversion to and from data in Javascript
object notation (JSON) format.  This allows R objects to be inserted into
Javascript/ECMAScript/ActionScript code and allows R programmers to read
and convert JSON content to R objects.  This is an alternative to rjson
package. That version was too slow for converting large R objects to JSON
and is not extensible, but a very useful prototype.  It is fast for
parsing.  This package uses methods, vectorized operations and C code and
callbacks to R functions for deserializing JSON objects to R.  Verison 0.4
of this package uses a new native parser, implements the transformation
code in C and allocates memory efficiently (rather than concatenating
because of event driven parsing).  The result is a significantly faster
parsing of large JSON documents.

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
%doc %{rlibdir}/RJSONIO/html
%doc %{rlibdir}/RJSONIO/DESCRIPTION
%doc %{rlibdir}/RJSONIO/doc
%{rlibdir}/RJSONIO/libs
%{rlibdir}/RJSONIO/Meta
%{rlibdir}/RJSONIO/help
%{rlibdir}/RJSONIO/NAMESPACE
%{rlibdir}/RJSONIO/sampleData
%{rlibdir}/RJSONIO/INDEX
%{rlibdir}/RJSONIO/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.96.0-1
- initial package for Fedora