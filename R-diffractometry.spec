%global packname  diffractometry
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.03
Release:          1%{?dist}
Summary:          Baseline identification and peak decomposition for x-ray diffractograms

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-03.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Residual-based baseline identification and peak decomposition for x-ray
diffractograms as introduced in Davies/Gather/Mergel/Meise/Mildenberger

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
%doc %{rlibdir}/diffractometry/html
%doc %{rlibdir}/diffractometry/DESCRIPTION
%{rlibdir}/diffractometry/help
%{rlibdir}/diffractometry/NAMESPACE
%{rlibdir}/diffractometry/libs
%{rlibdir}/diffractometry/data
%{rlibdir}/diffractometry/R
%{rlibdir}/diffractometry/INDEX
%{rlibdir}/diffractometry/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.03-1
- initial package for Fedora