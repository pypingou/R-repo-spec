%global packname  egonet
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{dist}
Summary:          Tool for ego-centric measures in Social Network Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-sna 

BuildRequires:    R-devel tex(latex) R-sna 

%description
A small tool for Social Network Analysis, dealing with ego-centric network
measures, including Burt's effective size and aggregate constraint and an
import code suitable for a large number of adjacency matrices. This
package depends on sna but does not automatically import it during
installation. Therefore if sna is not already present in your system,
install it.

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
%doc %{rlibdir}/egonet/DESCRIPTION
%doc %{rlibdir}/egonet/html
%{rlibdir}/egonet/help
%{rlibdir}/egonet/NAMESPACE
%{rlibdir}/egonet/R
%{rlibdir}/egonet/INDEX
%{rlibdir}/egonet/Meta

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- Update to version 1.1

* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora