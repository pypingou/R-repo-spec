%global packname  fuzzyOP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1
Release:          1%{?dist}
Summary:          Fuzzy numbers and the main mathematical operations

Group:            Applications/Engineering 
License:          GPL (>=2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package contains functions which allow the depiction of fuzzy
numbers. Besides, the main arithmetic operations are applied to fuzzy
numbers and the extension principle for continuous functions can be
applied and plotted.

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
%doc %{rlibdir}/fuzzyOP/html
%doc %{rlibdir}/fuzzyOP/DESCRIPTION
%{rlibdir}/fuzzyOP/R
%{rlibdir}/fuzzyOP/NAMESPACE
%{rlibdir}/fuzzyOP/INDEX
%{rlibdir}/fuzzyOP/help
%{rlibdir}/fuzzyOP/data
%{rlibdir}/fuzzyOP/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1-1
- initial package for Fedora