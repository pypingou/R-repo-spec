%global packname  JOP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.0
Release:          1%{?dist}
Summary:          Joint Optimization Plot

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rsolnp R-rgenoud R-stats R-JointModeling 

BuildRequires:    R-devel tex(latex) R-Rsolnp R-rgenoud R-stats R-JointModeling 

%description
JOP is a tool for simultanous optimization of multiple responses and
visualization of the results. The visualization is done by the joint
optimization plot introduced by Kuhnt and Erbruegge (2004).

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
%doc %{rlibdir}/JOP/html
%doc %{rlibdir}/JOP/DESCRIPTION
%{rlibdir}/JOP/R
%{rlibdir}/JOP/NAMESPACE
%{rlibdir}/JOP/help
%{rlibdir}/JOP/INDEX
%{rlibdir}/JOP/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.0-1
- initial package for Fedora