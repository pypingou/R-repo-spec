%global packname  Rniftilib
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.29
Release:          1%{?dist}
Summary:          Rniftilib - R Interface to NIFTICLIB (V1.1.0)

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-29.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
R interface to nifticlib (nifticlib-1.1.0) (read/write
ANALYZE(TM)7.5/NIfTI-1 volume images)

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
%doc %{rlibdir}/Rniftilib/DESCRIPTION
%doc %{rlibdir}/Rniftilib/html
%{rlibdir}/Rniftilib/NAMESPACE
%{rlibdir}/Rniftilib/INDEX
%{rlibdir}/Rniftilib/help
%{rlibdir}/Rniftilib/Meta
RPM build errors:
%{rlibdir}/Rniftilib/R
%{rlibdir}/Rniftilib/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.29-1
- initial package for Fedora