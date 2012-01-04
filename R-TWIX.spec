%global packname  TWIX
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.10
Release:          1%{?dist}
Summary:          Trees WIth eXtra splits

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Trees with extra splits

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
%doc %{rlibdir}/TWIX/html
%doc %{rlibdir}/TWIX/DESCRIPTION
%{rlibdir}/TWIX/NAMESPACE
%{rlibdir}/TWIX/Meta
%{rlibdir}/TWIX/R
%{rlibdir}/TWIX/help
%{rlibdir}/TWIX/libs
%{rlibdir}/TWIX/INDEX
%{rlibdir}/TWIX/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.10-1
- initial package for Fedora