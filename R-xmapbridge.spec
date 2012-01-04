%global packname  xmapbridge
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.12.0
Release:          1%{?dist}
Summary:          Export plotting files to the xmapBridge for visualisation in X:Map

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
xmapBridge can plot graphs in the X:Map genome browser. This package
exports plotting files in a suitable format.

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
%doc %{rlibdir}/xmapbridge/DESCRIPTION
%doc %{rlibdir}/xmapbridge/html
%doc %{rlibdir}/xmapbridge/CITATION
%doc %{rlibdir}/xmapbridge/doc
%{rlibdir}/xmapbridge/unitTests
%{rlibdir}/xmapbridge/help
%{rlibdir}/xmapbridge/Meta
%{rlibdir}/xmapbridge/INDEX
%{rlibdir}/xmapbridge/data
%{rlibdir}/xmapbridge/R
%{rlibdir}/xmapbridge/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.12.0-1
- initial package for Fedora