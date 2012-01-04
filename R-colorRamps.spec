%global packname  colorRamps
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.3
Release:          1%{?dist}
Summary:          Builds color tables

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Builds gradient color maps

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
%doc %{rlibdir}/colorRamps/DESCRIPTION
%doc %{rlibdir}/colorRamps/html
%{rlibdir}/colorRamps/help
%{rlibdir}/colorRamps/NAMESPACE
%{rlibdir}/colorRamps/R
%{rlibdir}/colorRamps/INDEX
%{rlibdir}/colorRamps/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3-1
- initial package for Fedora