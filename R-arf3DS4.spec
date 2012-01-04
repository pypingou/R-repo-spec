%global packname  arf3DS4
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.5.4
Release:          1%{?dist}
Summary:          Activated Region Fitting, fMRI data analysis (3D).

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.5-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-graphics R-tcltk 

BuildRequires:    R-devel tex(latex) R-methods R-graphics R-tcltk 

%description
Activated Region Fitting (ARF) is an analysis method for fMRI data.

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
%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.5.4-1
- initial package for Fedora