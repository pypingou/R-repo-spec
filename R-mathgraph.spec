%global packname  mathgraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.10
Release:          1%{?dist}
Summary:          Directed and undirected graphs

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Simple tools for constructing and manipulating objects of class mathgraph
from the book "S Poetry", available at

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
%doc %{rlibdir}/mathgraph/html
%doc %{rlibdir}/mathgraph/DESCRIPTION
%{rlibdir}/mathgraph/help
%{rlibdir}/mathgraph/Meta
%{rlibdir}/mathgraph/NAMESPACE
%{rlibdir}/mathgraph/R
%{rlibdir}/mathgraph/INDEX
%{rlibdir}/mathgraph/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.10-1
- initial package for Fedora