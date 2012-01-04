%global packname  dynamicGraph
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.2.6
Release:          1%{?dist}
Summary:          dynamicGraph

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-ggm R-tcltk 

BuildRequires:    R-devel tex(latex) R-methods R-ggm R-tcltk 

%description
Interactive graphical tool for manipulating graphs

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
%doc %{rlibdir}/dynamicGraph/html
%doc %{rlibdir}/dynamicGraph/DESCRIPTION
%{rlibdir}/dynamicGraph/old.demos
%{rlibdir}/dynamicGraph/demo
%{rlibdir}/dynamicGraph/Meta
%{rlibdir}/dynamicGraph/NAMESPACE
%{rlibdir}/dynamicGraph/demo.source
%{rlibdir}/dynamicGraph/help
%{rlibdir}/dynamicGraph/INDEX
%{rlibdir}/dynamicGraph/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2.6-1
- initial package for Fedora