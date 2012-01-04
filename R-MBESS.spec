%global packname  MBESS
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          3.2.1
Release:          1%{?dist}
Summary:          MBESS

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
MBESS implements methods that are especially useful to researchers working
within the behavioral, educational, and social sciences (both substantive
researchers and methodologists), Many of the methods contained within
MBESS are applicable to quantitative research in general,

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
%doc %{rlibdir}/MBESS/DESCRIPTION
%doc %{rlibdir}/MBESS/html
%{rlibdir}/MBESS/Meta
%{rlibdir}/MBESS/help
%{rlibdir}/MBESS/INDEX
%{rlibdir}/MBESS/data
%{rlibdir}/MBESS/R
%{rlibdir}/MBESS/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 3.2.1-1
- initial package for Fedora