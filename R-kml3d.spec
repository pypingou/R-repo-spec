%global packname  kml3d
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.6
Release:          1%{?dist}
Summary:          K-means for joint Longitudinal data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-methods R-clv R-rgl R-misc3d 


BuildRequires:    R-devel tex(latex) R-methods R-clv R-rgl R-misc3d



%description
KmL3D is an implementation of k-means specificaly design to deal with
joint longitudinal data (longitudinal data on several variable). It
provide facilities to deal with missing value and propose a graphical
interphace for chosing the correct number of clusters.

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
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.6-1
- initial package for Fedora