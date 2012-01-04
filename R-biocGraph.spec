%global packname  biocGraph
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.1
Release:          1%{?dist}
Summary:          Graph examples and use cases in Bioinformatics

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Rgraphviz R-graph 

BuildRequires:    R-devel tex(latex) R-Rgraphviz R-graph 

%description
This package provides examples and code that make use of the different
graph related packages produced by Bioconductor.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.1-1
- initial package for Fedora