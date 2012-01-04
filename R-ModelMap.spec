%global packname  ModelMap
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Creates Random Forest and Stochastic Gradient Boosting Models, and applies them to GIS .img files to build detailed prediction maps.

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-randomForest R-gbm R-PresenceAbsence R-rgdal R-fields 


BuildRequires:    R-devel tex(latex) R-randomForest R-gbm R-PresenceAbsence R-rgdal R-fields



%description
This package will create sophisticated models of training data and
validate the models with an independant test set, cross validation, or in
the case of Random Forest Models, with Out OF Bag (OOB) predictions on the
training data. It will creat graphs and tables of the model validation
results. It will apply these models to GIS .img files of predictors to
create detailed prediction surfaces. It will handle large predictor files
for map making, by reading in the .img files in chuncks, and output to the
.txt file the prediction for each data chunk, before reading the next
chenk of data.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.1-1
- initial package for Fedora