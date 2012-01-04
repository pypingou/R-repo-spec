%global packname  intergraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.0
Release:          1%{?dist}
Summary:          Coercion routines for network data objects in R

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-utils R-graphics R-network R-igraph 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-utils R-graphics R-network R-igraph 


%description
R world provides several packages for working with network data. This
package supplements that functionality by providing methods for converting
network data objects between classes defined in other packages. Currently
supported classes: network, igraph.

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
%doc %{rlibdir}/intergraph/CITATION
%doc %{rlibdir}/intergraph/DESCRIPTION
%doc %{rlibdir}/intergraph/html
%{rlibdir}/intergraph/NAMESPACE
%{rlibdir}/intergraph/Meta
%{rlibdir}/intergraph/help
%{rlibdir}/intergraph/LICENSE
%{rlibdir}/intergraph/data
%{rlibdir}/intergraph/utests
%{rlibdir}/intergraph/R
%{rlibdir}/intergraph/SVNREV
%{rlibdir}/intergraph/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.0-1
- initial package for Fedora