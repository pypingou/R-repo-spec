%global packname  lmodel2
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.0
Release:          1%{?dist}
Summary:          Model II Regression

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.7-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes model II simple linear regression using ordinary least squares
(OLS), major axis (MA), standard major axis (SMA), and ranged major axis

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
%doc %{rlibdir}/lmodel2/html
%doc %{rlibdir}/lmodel2/doc
%doc %{rlibdir}/lmodel2/DESCRIPTION
%{rlibdir}/lmodel2/R
%{rlibdir}/lmodel2/NAMESPACE
%{rlibdir}/lmodel2/help
%{rlibdir}/lmodel2/data
%{rlibdir}/lmodel2/Meta
%{rlibdir}/lmodel2/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.0-1
- initial package for Fedora