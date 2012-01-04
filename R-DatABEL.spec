%global packname  DatABEL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.2
Release:          1%{?dist}
Summary:          file-based access to large matrices stored on HDD in binary format

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
a package providing interface to C++ FILEVECTOR library facilitating
analysis of large (giga- to tera-bytes) matrices; matrix storage is
organized in a way that either columns or rows are quickly accessible;
primarily aimed to support genome-wide association analyzes e.g. using
GenABEL, MixABEL and ProbABEL

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
%doc %{rlibdir}/DatABEL/DESCRIPTION
%doc %{rlibdir}/DatABEL/doc
%doc %{rlibdir}/DatABEL/html
%{rlibdir}/DatABEL/unitTests
%{rlibdir}/DatABEL/libs
%{rlibdir}/DatABEL/INDEX
%{rlibdir}/DatABEL/Meta
%{rlibdir}/DatABEL/R
%{rlibdir}/DatABEL/NAMESPACE
%{rlibdir}/DatABEL/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.2-1
- initial package for Fedora