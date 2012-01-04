%global packname  censReg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Censored Regression (Tobit) Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.5-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-maxLik 
Requires:         R-glmmML R-sandwich 

BuildRequires:    R-devel tex(latex) R-maxLik
BuildRequires:    R-glmmML R-sandwich 


%description
Estimation of censored regression (Tobit) models with cross-section and
panel data

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
%doc %{rlibdir}/censReg/DESCRIPTION
%doc %{rlibdir}/censReg/NEWS
%doc %{rlibdir}/censReg/doc
%doc %{rlibdir}/censReg/html
%{rlibdir}/censReg/INDEX
%{rlibdir}/censReg/help
%{rlibdir}/censReg/Meta
%{rlibdir}/censReg/R
%{rlibdir}/censReg/NAMESPACE

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora