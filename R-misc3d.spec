%global packname  misc3d
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Miscellaneous 3D Plots

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
A collection of miscellaneous 3d plots, including isosurfaces.

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
%doc %{rlibdir}/misc3d/CITATION
%doc %{rlibdir}/misc3d/DESCRIPTION
%doc %{rlibdir}/misc3d/html
%{rlibdir}/misc3d/Meta
%{rlibdir}/misc3d/R
%{rlibdir}/misc3d/data
%{rlibdir}/misc3d/INDEX
%{rlibdir}/misc3d/help
%{rlibdir}/misc3d/demo
%{rlibdir}/misc3d/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora