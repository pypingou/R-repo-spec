%global packname  rtv
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.3
Release:          1%{?dist}
Summary:          Random Time Variables

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-s3x 

BuildRequires:    R-devel tex(latex) R-s3x 

%description
A package for conveniently representing, manipulating and visualising time
data. Here, time is regarded as a random variable, and objects are used to
represent realisations of that random variable. This is particularly
useful for change points, irregular timeseries and failure events. There's
a strong emphasis on continuous representations of time, with
user-specified origins and units.

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
%doc %{rlibdir}/rtv/html
%doc %{rlibdir}/rtv/DESCRIPTION
%doc %{rlibdir}/rtv/doc
%{rlibdir}/rtv/NAMESPACE
%{rlibdir}/rtv/INDEX
%{rlibdir}/rtv/Meta
%{rlibdir}/rtv/help
%{rlibdir}/rtv/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.3-1
- initial package for Fedora