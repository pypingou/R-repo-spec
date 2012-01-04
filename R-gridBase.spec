%global packname  gridBase
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Integration of base and grid graphics

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics R-grid 

BuildRequires:    R-devel tex(latex) R-graphics R-grid 

%description
Integration of base and grid graphics

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
%doc %{rlibdir}/gridBase/doc
%doc %{rlibdir}/gridBase/DESCRIPTION
%doc %{rlibdir}/gridBase/html
%{rlibdir}/gridBase/NAMESPACE
%{rlibdir}/gridBase/demo
%{rlibdir}/gridBase/R
%{rlibdir}/gridBase/INDEX
%{rlibdir}/gridBase/help
%{rlibdir}/gridBase/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.3-1
- initial package for Fedora