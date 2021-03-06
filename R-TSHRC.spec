%global packname  TSHRC
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Two Stage Hazard Rate Comparison

Group:            Applications/Engineering 
License:          X11
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
two-stage procedure for comparing hazard rate functions which may or may
not cross each other

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
%doc %{rlibdir}/TSHRC/DESCRIPTION
%doc %{rlibdir}/TSHRC/html
%{rlibdir}/TSHRC/libs
%{rlibdir}/TSHRC/Meta
%{rlibdir}/TSHRC/help
%{rlibdir}/TSHRC/INDEX
%{rlibdir}/TSHRC/data
%{rlibdir}/TSHRC/R
%{rlibdir}/TSHRC/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora