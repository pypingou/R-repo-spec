%global packname  Boruta
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          Boruta -- a tool for finding significant attributes in information systems

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-randomForest 

BuildRequires:    R-devel tex(latex) R-randomForest 

%description
Boruta is a feature selection algorithm based on a randomForest
classifier. It selects the full set of all relevant attributes by
comparing original attributes' importances with importance achievable at
random estimated using their randomised copies.

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
%doc %{rlibdir}/Boruta/COPYING
%doc %{rlibdir}/Boruta/CITATION
%doc %{rlibdir}/Boruta/DESCRIPTION
%doc %{rlibdir}/Boruta/html
%doc %{rlibdir}/Boruta/NEWS
%{rlibdir}/Boruta/NAMESPACE
%{rlibdir}/Boruta/help
%{rlibdir}/Boruta/R
%{rlibdir}/Boruta/Meta
%{rlibdir}/Boruta/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora