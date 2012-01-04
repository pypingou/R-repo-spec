%global packname  ontoCAT
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.6.0
Release:          1%{?dist}
Summary:          Ontology traversal and search

Group:            Applications/Engineering 
License:          Apache License 2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-rJava R-methods 

BuildRequires:    R-devel tex(latex) R-rJava R-methods 

%description
The ontoCAT R package provides a simple interface to ontologies described
in widely used standard formats, stored locally in the filesystem or
accessible online. The full version of ontoCAT R package also supports
searching for ontology terms across multiple ontologies and in major
ontology repositories, as well as a number of advanced ontology navigation
functions: www.ontocat.org/wiki/r

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.6.0-1
- initial package for Fedora