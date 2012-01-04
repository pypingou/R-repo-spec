%global packname  svSweave
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          SciViews GUI API - Sweave functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Supporting functions for the GUI API (Sweave functions)

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
%doc %{rlibdir}/svSweave/CITATION
%doc %{rlibdir}/svSweave/NEWS
%doc %{rlibdir}/svSweave/DESCRIPTION
%doc %{rlibdir}/svSweave/html
%{rlibdir}/svSweave/INDEX
%{rlibdir}/svSweave/R
%{rlibdir}/svSweave/help
%{rlibdir}/svSweave/NAMESPACE
%{rlibdir}/svSweave/LICENSE
%{rlibdir}/svSweave/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora