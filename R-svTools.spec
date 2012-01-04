%global packname  svTools
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.9.1
Release:          1%{?dist}
Summary:          SciViews GUI API - Tools (wrapper for packages tools and codetools)

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-utils R-tools R-codetools R-svMisc 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-utils R-tools R-codetools R-svMisc 


%description
Set of tools aimed at wrapping some of the functionalities of the packages
tools, utils and codetools into a nicer format so that an IDE can use them

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
%doc %{rlibdir}/svTools/html
%doc %{rlibdir}/svTools/NEWS
%doc %{rlibdir}/svTools/CITATION
%doc %{rlibdir}/svTools/DESCRIPTION
%{rlibdir}/svTools/NAMESPACE
%{rlibdir}/svTools/LICENSE
%{rlibdir}/svTools/Meta
%{rlibdir}/svTools/help
%{rlibdir}/svTools/R
%{rlibdir}/svTools/data
%{rlibdir}/svTools/INDEX

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.1-1
- initial package for Fedora