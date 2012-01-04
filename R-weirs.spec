%global packname  weirs
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.21
Release:          1%{?dist}
Summary:          A Hydraulics Package to Compute Open-Channel Flow over Weirs

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-utils 

BuildRequires:    R-devel tex(latex) R-utils 

%description
This hydraulics package provides computational support for flow over
weirs, such as sharp-crested, broad-crested, and embankments. Initially,
the package supports broad- and sharp-crested weirs.

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
%doc %{rlibdir}/weirs/CITATION
%doc %{rlibdir}/weirs/DESCRIPTION
%doc %{rlibdir}/weirs/html
%{rlibdir}/weirs/R
%{rlibdir}/weirs/NAMESPACE
%{rlibdir}/weirs/INDEX
%{rlibdir}/weirs/WARRANTY
%{rlibdir}/weirs/help
%{rlibdir}/weirs/Meta
%{rlibdir}/weirs/Nomographs4R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.21-1
- initial package for Fedora