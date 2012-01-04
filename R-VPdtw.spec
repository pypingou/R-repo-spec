%global packname  VPdtw
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.8
Release:          1%{?dist}
Summary:          Variable Penalty Dynamic Time Warping

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Variable Penalty Dynamic Time Warping for aligning GC-MS chromatograms to
a master signal and more. With the appropriate penalty this method
performs good alignment without altering the shape of peaks in GC-MS data.

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
%doc %{rlibdir}/VPdtw/DESCRIPTION
%doc %{rlibdir}/VPdtw/CITATION
%doc %{rlibdir}/VPdtw/html
%{rlibdir}/VPdtw/data
%{rlibdir}/VPdtw/libs
%{rlibdir}/VPdtw/Meta
%{rlibdir}/VPdtw/NAMESPACE
%{rlibdir}/VPdtw/R
%{rlibdir}/VPdtw/INDEX
%{rlibdir}/VPdtw/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.8-1
- initial package for Fedora