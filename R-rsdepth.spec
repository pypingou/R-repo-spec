%global packname  rsdepth
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Ray Shooting Depth (i.e. RS Depth) functions for bivariate analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Ray Shooting Depth functions are provided for bivariate analysis.

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
%doc %{rlibdir}/rsdepth/html
%doc %{rlibdir}/rsdepth/DESCRIPTION
%{rlibdir}/rsdepth/INDEX
%{rlibdir}/rsdepth/R
%{rlibdir}/rsdepth/NAMESPACE
%{rlibdir}/rsdepth/libs
%{rlibdir}/rsdepth/help
%{rlibdir}/rsdepth/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora