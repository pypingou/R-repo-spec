%global packname  moduleColor
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.08.1
Release:          1%{?dist}
Summary:          Basic module functions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.08-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-stats R-impute R-grDevices R-dynamicTreeCut 

BuildRequires:    R-devel tex(latex) R-stats R-impute R-grDevices R-dynamicTreeCut 

%description
Methods for color labeling, calculation of eigengenes, merging of closely
related modules.

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
%doc %{rlibdir}/moduleColor/DESCRIPTION
%doc %{rlibdir}/moduleColor/html
%{rlibdir}/moduleColor/INDEX
%{rlibdir}/moduleColor/help
%{rlibdir}/moduleColor/Meta
%{rlibdir}/moduleColor/R
%{rlibdir}/moduleColor/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.08.1-1
- initial package for Fedora