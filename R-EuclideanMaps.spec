%global packname  EuclideanMaps
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Displays Euclidean Maps

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-tkrplot R-RODBC 

BuildRequires:    R-devel tex(latex) R-tcltk R-tkrplot R-RODBC 

%description
Euclidean maps are graphical representations of the rows and columns of
the matrix Y, by row and column points points based on the estimated
parameters of the multiplicative interaction model (MI). These graphs
represent the Euclidean space structure of the rows and columns as points
of Rp and Rq, and thus allow diagnosis of the model that best fits the

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
%doc %{rlibdir}/EuclideanMaps/html
%doc %{rlibdir}/EuclideanMaps/DESCRIPTION
%{rlibdir}/EuclideanMaps/R
%{rlibdir}/EuclideanMaps/help
%{rlibdir}/EuclideanMaps/Meta
%{rlibdir}/EuclideanMaps/po
%{rlibdir}/EuclideanMaps/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora