%global packname  TypeInfo
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Optional Type Specification Prototype

Group:            Applications/Engineering 
License:          BSD
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
A prototype for a mechanism for specifying the types of parameters and the
return value for an R function. This is meta-information that can be used
to generate stubs for servers and various interfaces to these functions.
Additionally, the arguments in a call to a typed function can be validated
using the type specifications. We allow types to be specified as either i)
by class name using either inheritance -  is(x, className), or strict
instance of - class(x) %in% className, or ii) a dynamic test given as an R
expression which is evaluated at run-time. More precise information and
interesting tests can be done via ii), but it is harder to use this
information as meta-data as it requires more effort to interpret it and it
is of course run-time information. It is typically more meaningful.

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
%doc %{rlibdir}/TypeInfo/doc
%doc %{rlibdir}/TypeInfo/DESCRIPTION
%doc %{rlibdir}/TypeInfo/html
%{rlibdir}/TypeInfo/NAMESPACE
%{rlibdir}/TypeInfo/help
%{rlibdir}/TypeInfo/Meta
%{rlibdir}/TypeInfo/INDEX
%{rlibdir}/TypeInfo/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora