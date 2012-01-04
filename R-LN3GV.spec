%global packname  LN3GV
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.12.1
Release:          1%{?dist}
Summary:          LN3GV

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.12-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
The main function of this package is called `analyze'. This function is
used to apply the LNNMV*, LNNGV, LN3, LN3MV*, or LN3GV methods (Lund and
Nettleton, 2011), which are extensions and modifications of the LNN and
LNNMV methods used in the package `EBarrays'.

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
%doc %{rlibdir}/LN3GV/html
%doc %{rlibdir}/LN3GV/DESCRIPTION
%{rlibdir}/LN3GV/R
%{rlibdir}/LN3GV/libs
%{rlibdir}/LN3GV/NAMESPACE
%{rlibdir}/LN3GV/INDEX
%{rlibdir}/LN3GV/help
%{rlibdir}/LN3GV/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.12.1-1
- initial package for Fedora