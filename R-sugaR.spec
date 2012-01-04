%global packname  sugaR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.5
Release:          1%{?dist}
Summary:          Plots to help optimising diabetes therapy

Group:            Applications/Engineering 
License:          AGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-grDevices R-graphics 

BuildRequires:    R-devel tex(latex) R-stats R-grDevices R-graphics 

%description
The package provides a series of plots to integrate glucose levels, basal
rate, activities, events and carbohydrate uptake on a single page in a
humanely interpretable manner. It is meant for best-possibly representing
the content of a well-curated diabetes diary of up to a week's time or of
up to seven comparable days, from which conclusions for adjusting the
individual treatment shall be drawn.

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
%doc %{rlibdir}/sugaR/doc
%doc %{rlibdir}/sugaR/html
%doc %{rlibdir}/sugaR/DESCRIPTION
%{rlibdir}/sugaR/NAMESPACE
%{rlibdir}/sugaR/Meta
%{rlibdir}/sugaR/R
%{rlibdir}/sugaR/help
%{rlibdir}/sugaR/data
%{rlibdir}/sugaR/demo
%{rlibdir}/sugaR/LICENSE
%{rlibdir}/sugaR/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.5-1
- initial package for Fedora