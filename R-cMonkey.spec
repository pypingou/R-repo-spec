%global packname  cMonkey
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          4.8.5
Release:          1%{?dist}
Summary:          cMonkey intgrated biclustering algorithm

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
cMonkey integrated biclustering algorithm for learning co-regulated gene

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
%doc %{rlibdir}/cMonkey/DESCRIPTION
%doc %{rlibdir}/cMonkey/html
%{rlibdir}/cMonkey/NAMESPACE
%{rlibdir}/cMonkey/INDEX
%{rlibdir}/cMonkey/Meta
%{rlibdir}/cMonkey/help
%{rlibdir}/cMonkey/R

%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.8.5-1
- initial package for Fedora