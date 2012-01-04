%global packname  qtlmt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.2
Release:          1%{?dist}
Summary:          Tools for mapping multiple complex traits

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This software provides tools for simultaneous analysis of multiple traits
in a backcross (BC) or recombinant inbred lines (RIL) population. It can
be used to select an optimal subset of traits for multiple-trait mapping,
analyze multiple traits via the SURE model and perform multiple-trait
composite multiple-interval mapping.

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
%doc %{rlibdir}/qtlmt/html
%doc %{rlibdir}/qtlmt/DESCRIPTION
%{rlibdir}/qtlmt/data
%{rlibdir}/qtlmt/NAMESPACE
%{rlibdir}/qtlmt/help
%{rlibdir}/qtlmt/Meta
%{rlibdir}/qtlmt/R
%{rlibdir}/qtlmt/libs
%{rlibdir}/qtlmt/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.2-1
- initial package for Fedora