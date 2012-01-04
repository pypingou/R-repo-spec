%global packname  GOstats
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.20.0
Release:          1%{?dist}
Summary:          Tools for manipulating GO and microarrays.

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-Category R-graph 

BuildRequires:    R-devel tex(latex) R-Biobase R-Category R-graph 

%description
A set of tools for interacting with GO and microarray data. A variety of
basic manipulation tools for graphs, hypothesis testing and other simple

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.20.0-1
- initial package for Fedora