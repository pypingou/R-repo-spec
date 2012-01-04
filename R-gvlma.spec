%global packname  gvlma
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0.1
Release:          1%{?dist}
Summary:          Global Validation of Linear Models Assumptions

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Methods from the paper: Pena, EA and Slate, EH, "Global Validation of
Linear Model Assumptions," J. American Statistical Association,
101(473):341-354, 2006.

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
%doc %{rlibdir}/gvlma/DESCRIPTION
%doc %{rlibdir}/gvlma/html
%{rlibdir}/gvlma/INDEX
%{rlibdir}/gvlma/Meta
%{rlibdir}/gvlma/NAMESPACE
%{rlibdir}/gvlma/R
%{rlibdir}/gvlma/data
%{rlibdir}/gvlma/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0.1-1
- initial package for Fedora