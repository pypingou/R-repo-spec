%global packname  Rgraphviz
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.32.0
Release:          1%{?dist}
Summary:          Provides plotting capabilities for R graph objects

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-utils R-graph R-grid 
Requires:         R-graph R-graphics R-grDevices R-grid R-methods R-utils 

BuildRequires:    R-devel tex(latex) R-methods R-utils R-graph R-grid
BuildRequires:    R-graph R-graphics R-grDevices R-grid R-methods R-utils 


%description
Interfaces R with the AT and T graphviz library for plotting R graph
objects from the graph package. Users on all platforms must install
graphviz; see the README file, available in the source distribution of
this file, for details.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.32.0-1
- initial package for Fedora